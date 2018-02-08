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
    return this.http.get(
      'users/',
    ).map((res: Response) => {
      data = res.json();
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
      'users/', { data }
    ).map((res: Response) => {
      data = res.json();
      if (!data.errors) {
        // Setting token after login
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
    return this.http.get('users/logout')
      .map((res: Response) => {
        localStorage.removeItem("user");
        localStorage.removeItem("id_token");
        localStorage.removeItem("expires_at");
        this.store.dispatch(this.actions.logoutSuccess());
        return res.json();
      });
  }

  isLoggedIn() {
    return moment().isBefore(this.getExpiration());
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
  private setLocalData(user_data: {user: User, idToken: string, expiresIn: string}): void {
    const jsonData = JSON.stringify(user_data);
    const expiresAt = moment().add(user_data.expiresIn, 'second');
    localStorage.setItem('user', jsonData);
    localStorage.setItem('id_token', user_data.idToken);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()) );
  }

  getExpiration() {
    const expiration = localStorage.getItem("expires_at");
    const expiresAt = JSON.parse(expiration);
    return moment(expiresAt);
  }
}
