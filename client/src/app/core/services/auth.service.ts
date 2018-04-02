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
import { JwtHelperService } from '@auth0/angular-jwt';
import { Router } from '@angular/router';
import { NotificationService } from '../../shared/components/notification/notification.service';
import {UserService} from "./user.service";
// Todo import { AuthActions } from '../../auth/actions/auth.actions';

function _window(): any {
  // return the global native browser window object
  return window;
}

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
    private store: Store<AppState>,
    private jwtHelper: JwtHelperService,
    private router: Router,
    private notifications: NotificationService,
    private userService: UserService
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
        this.notifications.sendMessage('Authorization', 'success', 'Signed in successfully', 5000)
      } else {
        this.http.loading.next({
          loading: false,
          error: {
            title: 'Please enter valid Credentials',
            message: 'Username or password is incorrect'
          }
        });
      }
      return data;
    }).shareReplay();
  }


  telegramRegister(): Observable<any> {
    return this.http.post('users/telegram/', {}).map(data => {
      // console.log(data);
      return data.json();
    });
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
        // console.log (res);

        this.setLocalData(res.json());
        this.store.dispatch(this.actions.loginSuccess(_data));
        this.notifications.sendMessage('Registration', 'success', 'Signed up successfully', 5000);
      } else {
        if (_data.data.username) {
          this.notifications.sendMessage('Enter valid credentials', 'error', 'This username is already registered', 5000);
        }
        if (_data.data.email) {
          this.notifications.sendMessage('Enter valid credentials', 'error', 'This email is already registered', 5000);
        }
        if (_data.data.password1) {
          this.notifications.sendMessage('Enter valid credentials', 'error', 'Password is too common', 5000);
        }
        // this.http.loading.next({
        //   loading: false,
        //   error: {
        //     title: 'Please enter valid Credentials',
        //   }
        // });
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
    return this.http.post('users/logout/', {})
      .map((res: Response) => {
        localStorage.removeItem("user");
        localStorage.removeItem("token");
        this.store.dispatch(this.actions.logoutSuccess());
        this.router.navigate(['auth', 'login']);
        this.notifications.sendMessage('Logout', 'success', 'Logged out successfully', 5000)
        return res.json();
      });
  }

  isLoggedIn() {
    return !!this.getToken();
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }

  getToken() {
    const token = localStorage.getItem('token');
    if (token && !this.jwtHelper.isTokenExpired(token)) {
      return token
    } else {
      this.logout();
      return null;
    }
  }
  getUserData() {
    const token = localStorage.getItem('token');
    if (token && !this.jwtHelper.isTokenExpired(token)) {
      return JSON.parse(localStorage.getItem('user')) as User;
    } else {
      this.logout();
      return null;
    }
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


  getNativeWindow(): any {
    return _window();
  }


}
