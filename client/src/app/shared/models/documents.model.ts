import { Author } from './authors.model';
import { Tag } from './tags.model';
import { Copy } from './copies.model';
import { Bestseller } from './bestsellers.model';

export class Document {
  document_id: number;
  title: string = "";
  description?: string = "";
  publisher?: string = "";
  year: number = 2018;
  type: number;
  price: number;
  is_reference: boolean;
  copies_available: number;
  cover?: string;
  date_added: Date;
  authors?: Author[] = [];
  tags?: Tag[];
  copies?: Copy[];
  bestseller?: Bestseller;
}
