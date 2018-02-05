import { Document } from '../../shared/models/documents.model'
import { Map, Record, List } from 'immutable';

export interface DocumentState extends Map<string, any> {
  documentIds: List<number>;
  documentEntities: Map<number, Document>;
  selectedDocumentId: number;
  selectedDocument: Document;
}

export const DocumentStateRecord = Record({
  documentIds: List([]),
  documentEntities: Map({}),
  selectedDocumentId: null,
  selectedDocument: Map({})
});
