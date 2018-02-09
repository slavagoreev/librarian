import { Action, ActionReducer } from '@ngrx/store';
import jwtDecode from 'jwt-decode'
import { AuthActions } from '../actions/auth.actions';
import { AuthState, AuthStateRecord } from './auth.state';

export const initialState: AuthState = new AuthStateRecord() as AuthState;

export function reducer(state = initialState, { type, payload }: any): AuthState {
    switch (type) {
      case AuthActions.LOGIN_SUCCESS:
        return state.merge({
          token: payload.token,
          isAuthenticated: true
        }) as AuthState;
      case AuthActions.TOKEN_RECEIVED:
        return state.merge({
          token: payload.token,
        }) as AuthState;
      case AuthActions.LOGIN_FAILURE:
      case AuthActions.TOKEN_FAILURE:
        return state.merge({
          token: "",
          errors: payload.response || {'non_field_errors': payload.statusText},
          isAuthenticated: false
        }) as AuthState;

      case AuthActions.LOGOUT_SUCCESS:
        return state.merge({ isAuthenticated: false }) as AuthState;

      default:
        return state;
    }
  };
