import { createSelector } from 'reselect';
import { AppState } from '../../interfaces';
import { DocumentState } from './document.state';
import { Document } from '../../shared/models/documents.model';

// Base document state selector function
export function getDocumentState(state: AppState): DocumentState {
  console.log (state.documents);
  return state.documents;
}

// ******************** Individual selectors ***************************
export function fetchDocuments(state: DocumentState) {
  const ids = state.documentIds.toJS();
  const documentEntities = state.documentEntities.toJS()//forEach(doc => doc as Document);
  console.log (documentEntities);
  return ids.map(id => documentEntities[id]);
}

const fetchSelectedDocument = function (state: DocumentState): Document {
  return state.selectedDocument;
};

// *************************** PUBLIC API's ****************************
export const getSelectedtDocument = createSelector(getDocumentState, fetchSelectedDocument);
export const getDocuments = createSelector(getDocumentState, fetchDocuments);
