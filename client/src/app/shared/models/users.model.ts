import { Order } from './orders.model';
export class Users {
  user_id: number;
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
