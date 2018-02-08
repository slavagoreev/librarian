import { DocumentState, InitialDocumentState } from './document.state';
import { DocumentActions } from './document.actions';
import { Document } from '../../shared/models/documents.model';

export const initialState: DocumentState = new InitialDocumentState() as DocumentState;

export function reducer(state = initialState, { type, payload }: any): DocumentState {
  switch (type) {
    case DocumentActions.GET_DOCUMENT_DETAIL_SUCCESS:
      return state.merge({
        selectedDocument: payload
      }) as DocumentState;

    case DocumentActions.GET_ALL_DOCUMENTS_SUCCESS:
      const _documents: Document[] = payload.data;
      if (_documents && _documents.length > 0) {
        const documentIds: number[] = _documents.map(document => document.document_id);
        const documentEntities = _documents.reduce((documents: { [id: number]: Document }, document: Document) => {
          return Object.assign(documents, {
            [document.document_id]: document
          });
        }, { });
        return state.merge({
          documentIds: documentIds,
          documentEntities: documentEntities
        }) as DocumentState;
      } else return state;

    case DocumentActions.REMOVE_DOCUMENT_SUCCESS:
      const documentId = payload;
      const index = state.documentIds.indexOf(documentId);

      return state.merge({
        documentIds: state.documentIds.splice(index, 1),
        documentEntities: state.documentEntities.delete(documentId),
      }) as DocumentState;
    default:
      return state;
  }
};
