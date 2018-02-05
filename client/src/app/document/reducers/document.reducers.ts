import { DocumentState, DocumentStateRecord } from './document.state';
import { DocumentActions } from './document.actions';
import { Document } from '../../shared/models/documents.model';

export const initialState: DocumentState = new DocumentStateRecord() as DocumentState;

export function reducer(state = initialState, { type, payload }: any): DocumentState {
  switch (type) {
    case DocumentActions.GET_DOCUMENT_DETAIL_SUCCESS:
      return state.merge({
        selectedDocument: payload
      }) as DocumentState;

    case DocumentActions.GET_ALL_DOCUMENTS_SUCCESS:
      console.log (payload)
      const _documents: Document[] = payload.documents.data;
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

    default:
      return state;
  }
};
