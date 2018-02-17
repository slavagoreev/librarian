import { AppState } from './../../interfaces';
import { createSelector } from 'reselect';
import { AuthState } from './auth.state';

// Base product state function
function getAuthState(state: AppState): AuthState {
    return state.auth;
}

// ******************** Individual selectors ***************************
const fetchAuthStatus = function(state: AuthState): boolean {
  return state.isAuthenticated
};

const fetchUserRole = function(state: AuthState): number {
  return state.role;
};

const fetchToken = function (state: AuthState) {
  return state.token
};

const fetchErrors = function (state: AuthState) {
  return state.errors
}

// *************************** PUBLIC API's ****************************
export const getAuthStatus = createSelector(getAuthState, fetchAuthStatus);
export const getUserRole = createSelector(getAuthState, fetchUserRole);
export const getErrors = createSelector(getAuthState, fetchErrors);
