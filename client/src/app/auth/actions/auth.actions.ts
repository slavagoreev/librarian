import { Action } from '@ngrx/store';

export class AuthActions {
  static LOGIN_REQUEST = 'LOGIN_REQUEST';
  static LOGIN_FAILURE = 'LOGIN_FAILURE';
  static LOGIN_SUCCESS = 'LOGIN_SUCCESS';
  static LOGOUT_REQUEST = 'LOGOUT_REQUEST';
  static LOGOUT_SUCCESS = 'LOGOUT_SUCCESS';
  static TOKEN_REQUEST = 'TOKEN_REQUEST';
  static TOKEN_RECEIVED = 'TOKEN_RECEIVED';
  static TOKEN_FAILURE = 'TOKEN_FAILURE';

  login() {
    return { type: AuthActions.LOGIN_REQUEST };
  }

  loginFailure() {
    return { type: AuthActions.LOGIN_FAILURE };
  }

  loginSuccess() {
    return { type: AuthActions.LOGIN_SUCCESS};
  }

  logout() {
    return { type: AuthActions.LOGOUT_REQUEST };
  }

  logoutSuccess() {
    return { type: AuthActions.LOGOUT_SUCCESS };
  }

  getToken() {
    return { type: AuthActions.TOKEN_REQUEST };
  }

  tokenRecieved() {
    return { type: AuthActions.TOKEN_RECEIVED };
  }
}
