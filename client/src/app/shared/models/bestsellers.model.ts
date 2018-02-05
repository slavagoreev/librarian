import { Document } from './documents.model';
export class Bestseller {
  bestseller_id: number;
  document_id: number;
  document?: Document;
  background_color?: string;
}
