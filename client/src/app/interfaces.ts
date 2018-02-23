import { DocumentState } from './document/reducers/document.state';
import { AuthState } from './auth/reducers/auth.state';
import { UserState } from './user/reducers/user.state';

export interface AppState {
  documents: DocumentState;
  auth: AuthState
  user: UserState
}
