import { Map, Record } from 'immutable';

export interface AuthState extends Map<string, any> {
  isAuthenticated: boolean;
  access: { token: string, exp?: number },
  refresh: { token: string, exp?: number },
  errors: {},
}

export const AuthStateRecord = Record({
  isAuthenticated: false,
  access: undefined,
  refresh: undefined,
  errors: {},
});
