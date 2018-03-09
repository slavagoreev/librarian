import {User} from "./users.model";

export class Order {
  order_id: number;
  document: Document;
  user: User;
  date_created: Date;
  date_accepted: Date;
  date_return: Date;
  status: number;
  overdue_sum: number;
  is_extendable?: boolean;
}
