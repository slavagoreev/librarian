import { Order } from './orders.model';
export class User {
  id: number;
  username: string;
  email: string;
  password?: string;
  password_salt?: string;
  role: number;
  first_name?: string;
  last_name?: string;
  address?: string;
  phone?: number;
  orders?: Order[];
}
