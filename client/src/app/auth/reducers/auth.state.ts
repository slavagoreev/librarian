import { Map, Record } from 'immutable';

export interface AuthState extends Map<string, any> {
  isAuthenticated: boolean;
  token: string,
  errors: {},
}

export const AuthStateRecord = Record({
  isAuthenticated: false,
  token: "",
  errors: {},
});
