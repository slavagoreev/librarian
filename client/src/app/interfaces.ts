import { DocumentState } from './document/reducers/document.state';
import { AuthState } from './auth/reducers/auth.state';

export interface AppState {
  documents: DocumentState;
  auth: AuthState
}
