import { Component, OnInit } from '@angular/core';
import { UserService } from "../../../core/services/user.service";
import { Observable } from "rxjs/Observable";
import { Order } from "../../../shared/models/orders.model";
import { Subscription } from "rxjs/Subscription";
import { DocumentService } from "../../../core/services/document.service";

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss']
})
export class OrdersComponent implements OnInit {

  orders$: Observable<Order[]>;

  constructor(
    private userService: UserService,
  ) {
  }

  ngOnInit() {
    this.userService.getOrders().subscribe(res => {
        this.orders$ = Observable.of(res);
      }
    );
  }
  statusStr(status: number){
    if (status == 0) return 'Requested';
    if (status == 1) return 'Booked';
    if (status == 2) return 'Overdue';
    if (status == 3) return 'Closed';
    if (status == 4) return 'Extended';
  }

}
