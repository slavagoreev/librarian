import { AppState } from './../../interfaces';
import { createSelector } from 'reselect';
import { AuthState } from './auth.state';

// Base product state function
function getAuthState(state: AppState): AuthState {
    return state.auth;
}

// ******************** Individual selectors ***************************
const fetchAuthStatus = function(state: AuthState): boolean {
  return fetchToken(state) !== ""
};

const fetchToken = function (state: AuthState) {
  return state.token
};

const fetchErrors = function (state: AuthState) {
  return state.errors
}

// *************************** PUBLIC API's ****************************
export const getAuthStatus = createSelector(getAuthState, fetchAuthStatus);
export const getAccessToken = createSelector(getAuthState, fetchToken);
export const getErrors = createSelector(getAuthState, fetchErrors);
