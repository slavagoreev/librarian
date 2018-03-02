import { Component, OnInit } from '@angular/core';
import { UserService } from "../../core/services/user.service";
import {Observable} from "rxjs/Observable";
import {Order} from "../../shared/models/orders.model";

@Component({
  selector: 'app-order-list',
  templateUrl: './order-list.component.html',
  styleUrls: ['./order-list.component.scss']
})
export class OrderListComponent implements OnInit {

  type = 'book';
  orders$: Observable<Order[]>;

  constructor(
    private userService: UserService
  ) {
    this.orders$ = userService.getAllOrders();
  }

  search() {
    this.orders$ = this.userService.getAllOrders();
  }

  selectType(type: string) {
    this.type = type;
  }

  selectStatus(id: number, status: number) {
    this.userService.setStatusForOrder(id, status).subscribe();
    this.orders$ = this.userService.getAllOrders();
  }

  statusStr(status: number){
    if (status == 0) return 'Requested';
    if (status == 1) return 'Booked';
    if (status == 2) return 'Overdue';
    if (status == 3) return 'Closed';
    if (status == 4) return 'Extended';
  }

  ngOnInit() {
  }

}
