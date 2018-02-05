import { Action } from '@ngrx/store';
import { Document } from '../../shared/models/documents.model';

export class DocumentActions {
  static GET_ALL_DOCUMENTS = 'GET_ALL_DOCUMENTS';
  static GET_ALL_DOCUMENTS_SUCCESS = 'GET_ALL_DOCUMENTS_SUCCESS';
  static GET_DOCUMENT_DETAIL = 'GET_DOCUMENT_DETAIL';
  static GET_DOCUMENT_DETAIL_SUCCESS = 'GET_DOCUMENT_DETAIL_SUCCESS';
  static CLEAR_SELECTED_DOCUMENT = 'CLEAR_SELECTED_DOCUMENT';

  getAllDocuments() {
    return { type: DocumentActions.GET_ALL_DOCUMENTS };
  }

  getDocumentDetail(id: string) {
    return {
      type: DocumentActions.GET_DOCUMENT_DETAIL,
      payload: id
    };
  }

  // change documents type to Document[]
  getAllDocumentsSuccess(documents: any) {
    return {
      type: DocumentActions.GET_ALL_DOCUMENTS_SUCCESS,
      payload: documents
    };
  }

  getDocumentDetailSuccess(document: Document) {
    return {
      type: DocumentActions.GET_DOCUMENT_DETAIL_SUCCESS,
      payload: document
    };
  }

  clearSelectedDocument() {
    return { type: DocumentActions.CLEAR_SELECTED_DOCUMENT };
  }
}
