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
      'api/users/login/', { data }
    ).map((res: Response) => {
      data = res.json();
      console.log (data);
      if (!data.error) {
        // Setting token after login
        this.setLocalData(data);
        this.store.dispatch(this.actions.loginSuccess());
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
      'api/users/registration/', data
    ).map((res: Response) => {
      data = res.json();
      if (!data.errors) {
        // Setting token after login
        console.log (res);
        this.setLocalData(res.json());
        this.store.dispatch(this.actions.loginSuccess());
      } else {
        this.http.loading.next({
          loading: false,
          hasError: true,
          hasMsg: 'Please enter valid Credentials'
        });
      }
      return res.json();
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
    return this.http.post('api/users/logout', {})
      .map((res: Response) => {
        localStorage.removeItem("user");
        localStorage.removeItem("token");
        this.store.dispatch(this.actions.logoutSuccess());
        return res.json();
      });
  }

  isLoggedIn() {
    return localStorage.getItem('token');
  }

  isLoggedOut() {
    return !this.isLoggedIn();
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
    const jsonData = JSON.stringify(user_data);
    localStorage.setItem('user', jsonData);
    localStorage.setItem('token', user_data.token);
  }
}
