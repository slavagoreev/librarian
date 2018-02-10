import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs/Observable';
import { Response } from '@angular/http';
import { AppState } from '../../interfaces';
import { Store } from '@ngrx/store';
import { HttpService } from './http.service';
import { AuthActions } from '../../auth/actions/auth.actions';
import { User } from '../../shared/models/users.model';
import * as moment from 'moment';
import _date = moment.unitOfTime._date;
// Todo import { AuthActions } from '../../auth/actions/auth.actions';

@Injectable()
export class AuthService {

  /**
   * Creates an instance of AuthService.
   * @param {HttpService} http
   * @param {AuthActions} actions
   * @param {Store<AppState>} store
   *
   * @memberof AuthService
   */
  constructor(
    private http: HttpService,
    private actions: AuthActions,
    private store: Store<AppState>
  ) {

  }

  /**
   *
   *
   * @param {any} data
   * @returns {Observable<any>}
   *
   * @memberof AuthService
   */
  login(data): Observable<any> {
    return this.http.post(
      'users/login/', data
    ).map((res: Response) => {
      data = res.json();
      console.log (data);
      if (data.token) {
        // Setting token after login
        this.setLocalData(data);
        this.store.dispatch(this.actions.loginSuccess(data));
      } else {
        this.http.loading.next({
          loading: false,
          hasError: true,
          hasMsg: 'Please enter valid Credentials'
        });
      }
      return data;
    }).shareReplay();
  }

  /**
   *
   *
   * @param {any} data
   * @returns {Observable<any>}
   *
   * @memberof AuthService
   */
  register(data): Observable<any> {
    return this.http.post(
      'users/registration/', data
    ).map((res: Response) => {
      const _data = res.json();
      if (_data.token) {
        // Setting token after login
        console.log (res);
        this.setLocalData(res.json());
        this.store.dispatch(this.actions.loginSuccess(_data));
      } else {
        this.http.loading.next({
          loading: false,
          hasError: true,
          hasMsg: 'Please enter valid Credentials'
        });
      }
      return _data;
    });
  }


  /**
   *
   *
   * @returns
   *
   * @memberof AuthService
   */

  logout() {
    return this.http.post('users/logout', {})
      .map((res: Response) => {
        localStorage.removeItem("user");
        localStorage.removeItem("token");
        this.store.dispatch(this.actions.logoutSuccess());
        return res.json();
      });
  }

  isLoggedIn() {
    return !!localStorage.getItem('token');
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }

  getToken() {
    return localStorage.getItem('token');
  }
  getUserData() {
    return JSON.parse(localStorage.getItem('user')) as User;
  }
  /**
   *
   *
   * @private
   * @param {any} user_data
   *
   * @memberof AuthService
   */
  private setLocalData(user_data: {user: User, token: string}): void {
    const jsonData = JSON.stringify(user_data.user);
    localStorage.setItem('user', jsonData);
    localStorage.setItem('token', user_data.token);
  }
}
