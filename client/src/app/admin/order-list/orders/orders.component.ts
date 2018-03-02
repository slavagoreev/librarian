import { Component, OnInit } from '@angular/core';
import {UserService} from "../../../core/services/user.service";
import {Observable} from "rxjs/Observable";
import {Order} from "../../../shared/models/orders.model";
import {Subscription} from "rxjs/Subscription";
import {DocumentService} from "../../../core/services/document.service";

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss']
})
export class OrdersComponent implements OnInit {

  orders$: Observable<Order[]>;
  actionsSubscription: Subscription;

  constructor(
    private userService: UserService,
  ) {
    this.orders$ = userService.getOrders();
  }

  ngOnInit() {
  }

}
