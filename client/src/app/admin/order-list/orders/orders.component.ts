import { Component, OnInit } from '@angular/core';
import { UserService } from "../../../core/services/user.service";
import { Observable } from "rxjs/Observable";
import { Order } from "../../../shared/models/orders.model";
import { Subscription } from "rxjs/Subscription";
import { DocumentService } from "../../../core/services/document.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss']
})
export class OrdersComponent implements OnInit {

  orders$: Observable<Order[]>;

  constructor(
    private userService: UserService,
    private router: Router
  ) {
  }

  ngOnInit() {
    this.reloadState();
  }

  reloadState() {
    this.userService.getOrders().subscribe(res => {
        this.orders$ = Observable.of(res);
      }
    );
  }
  statusStr(status: number) {
    if (status === 0) return 'Requested';
    if (status === 1) return 'Booked';
    if (status === 2) return 'Overdue';
    if (status === 3) return 'Closed';
    if (status === 4) return 'Extended';
  }
  goToDocument(document_id: number) {
    this.router.navigate(['/documents', document_id.toString()]);
  }

  formatTitle(title: string) {
    if (title.length > 49) {
      title = title.substr(0, 48) + "...";
    }
    return title;
  }
  extendOrder(id: number) {
    this.userService.setStatusForMyOrder(id, 4).subscribe(res => {
      this.userService.getOrders().subscribe(data => {
        this.orders$ = Observable.of(data);
        this.reloadState();
      });
    });
  }
}
