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

  isOrders = 1;
  type = 'book';
  orders$: Observable<Order[]>;

  constructor(
    private userService: UserService
  ) {
  }

  search() {
    this.orders$ = this.userService.getAllOrders();
  }

  selectType(type: string) {
    this.type = type;
  }

  selectStatus(id: number, status: number) {
    this.userService.setStatusForOrder(id, status).subscribe(res => {
      this.observeOrders();
    });
    this.userService.getAllOrders();
  }

  statusStr(status: number){
    if (status == 0) return 'Requested';
    if (status == 1) return 'Booked';
    if (status == 2) return 'Overdue';
    if (status == 3) return 'Closed';
    if (status == 4) return 'Extended';
  }

  /*
    <option value="100" [selected]="user.role === 100">Patron</option>
    <option value="210" [selected]="user.role === 210">Instructor</option>
    <option value="220" [selected]="user.role === 220">Teacher Assistant</option>
    <option value="230" [selected]="user.role === 230">Visiting Professor</option>
    <option value="240" [selected]="user.role === 240">Professor</option>
    <option value="300" [selected]="user.role === 300">Librarian</option>
   */
  getRole(role: number) {
    if (role === 100) {
      return "Stud.";
    }
    if (role === 210) {
      return "Inst.";
    }
    if (role === 220) {
      return "T.A";
    }
    if (role === 230) {
      return "V.P";
    }
    if (role === 240) {
      return "Prof.";
    }
    if (role === 300) {
      return "Libr.";
    }
  }

  observeOrders() {
    this.userService.getAllOrders().subscribe(res => {
      this.orders$ = Observable.of(res);
    });
  }

  observePreorders() {
    this.userService.getAllPreorders().subscribe(res => {
      this.orders$ = Observable.of(res);
    });
  }
  toOrders() {
    this.observeOrders();
    this.isOrders = 1;
  }

  toPreorders() {
    this.observePreorders();
    this.isOrders = 0;
  }

  ngOnInit() {
    this.observeOrders();
  }

}
