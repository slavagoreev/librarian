import { AppState } from './../../interfaces';
import { createSelector } from 'reselect';
import { AuthState } from './auth.state';

// Base product state function
function getAuthState(state: AppState): AuthState {
    return state.auth;
}

// ******************** Individual selectors ***************************
const fetchAuthStatus = function(state: AuthState): boolean {
  return !isRefreshTokenExpired(state)
};

const fetchAccessToken = function (state: AuthState) {
  if (state.access) {
    return  state.access.token
  }
};

const fetchRefreshToken = function (state: AuthState) {
  if (state.refresh) {
    return state.refresh.token
  }
};

const isAccessTokenExpired = function (state: AuthState) {
  if (state.access && state.access.exp) {
    return 1000 * state.access.exp - (new Date()).getTime() < 5000
  }
  return true
};
const isRefreshTokenExpired = function (state: AuthState) {
  if (state.refresh && state.refresh.exp) {
    return 1000 * state.refresh.exp - (new Date()).getTime() < 5000
  }
  return true
};
const fetchErrors = function (state: AuthState) {
  return state.errors
}

// *************************** PUBLIC API's ****************************
export const getAuthStatus = createSelector(getAuthState, fetchAuthStatus);
export const getAccessToken = createSelector(getAuthState, fetchAccessToken);
export const getRefreshToken = createSelector(getAuthState, fetchRefreshToken);
export const getErrors = createSelector(getAuthState, fetchErrors);
