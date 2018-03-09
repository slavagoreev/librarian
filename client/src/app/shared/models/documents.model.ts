import { Author } from './authors.model';
import { Tag } from './tags.model';
import { Copy } from './copies.model';

export class Document {
  document_id: number;
  title: string = "";
  description?: string = "";
  publisher?: string = "";
  year: number = 2018;
  document_type: number;
  price: number;
  is_reference: boolean;
  copies_available: number;
  cover?: string;
  // date_added: Date;
  authors?: Author[] = [];
  tags?: Tag[];
  copies?: Copy[];
  is_bestseller?: boolean;
  is_extendable?: boolean;
}
