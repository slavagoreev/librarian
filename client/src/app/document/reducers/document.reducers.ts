import { DocumentState, InitialDocumentState } from './document.state';
import { DocumentActions } from './document.actions';
import { Document } from '../../shared/models/documents.model';
import { List } from 'immutable';

export const initialState: DocumentState = new InitialDocumentState() as DocumentState;

export function reducer(state = initialState, { type, payload }: any): DocumentState {
  switch (type) {
    case DocumentActions.GET_DOCUMENT_DETAIL_SUCCESS:
      return state.merge({
        selectedDocument: payload
      }) as DocumentState;

    case DocumentActions.GET_ALL_DOCUMENTS_SUCCESS:
      const _documents: Document[] = payload;
      if (_documents && _documents.length > 0) {
        return state.merge({
          documentIds: state.documentIds.concat(_documents.map(document => document.document_id)),
          documentEntities: state.documentEntities.concat(
            _documents.reduce((documents: { [id: number]: Document }, document: Document) => {
              return Object.assign(documents, {
                [document.document_id]: document
              });
            }, {}))
        }) as DocumentState;
      } else return state;

    case DocumentActions.REMOVE_DOCUMENT_SUCCESS:
      const documentId = payload;
      const index = state.documentIds.indexOf(documentId);

      return state.merge({
        documentIds: state.documentIds.splice(index, 1),
        documentEntities: state.documentEntities.delete(documentId),
      }) as DocumentState;

    case DocumentActions.CLEAR_DOCUMENTS:
      return initialState as DocumentState;
    default:
      return state;
  }
};
