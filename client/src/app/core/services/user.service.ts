import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { Observable } from 'rxjs/Observable';
import { User } from '../../shared/models/users.model';
import { Order } from '../../shared/models/orders.model';
import { Headers, RequestMethod, RequestOptions } from '@angular/http';
import {Store} from '@ngrx/store';
import {AppState} from '../../interfaces';

@Injectable()
export class UserService {

  constructor(
    private http: HttpService,
    private store: Store<AppState>
  ) { }

  getUserData(id: number): Observable<User> {
    return this.http.get(`users/${id}`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load user details from server',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  setUserData(user): Observable<any> {
    return this.http.patch(`users/${user.id}`, user)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load user details from server',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  getUserList(): Observable<any> {
    return this.http.get(`users/`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load user list from server',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  getOrders(): Observable<Order[]> {
    return this.http.get(`myorders/`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load orders',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  getAllOrders(): Observable<Order[]> {
    return this.http.get(`orders/`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load orders',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  getOrderDetail(orderNumber): Observable<Order> {
    return this.http.get(`users/${orderNumber}`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load orders',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  bookTheDocument(documentId): Observable<Order> {
    return this.http.get(`booking/${documentId}`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Booking error',
              message: 'Could not book this document',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  setStatusForOrder(order_id: number, status: number): Observable<Order> {
    // options.body.set('status', status.toString());
    return this.http.patch(`orders/${order_id}`, {'status': status})
      .map(res => {
        const _res = res.json();
        // return _res.data;
        // console.error ("TODO");
        return null;
    });
  }

  setStatusForMyOrder(order_id: number, status: number): Observable<Order> {
    // options.body.set('status', status.toString());
    return this.http.patch(`myorders/${order_id}`, {'status': status})
      .map(res => {
        const _res = res.json();
        // return _res.data;
        // console.error ("TODO");
        return null;
      });
  }

  removeUser(id: number) {
    return this.http.delete(`users/${id.toString()}/`)
      .map((res) => {
        // return this.store.dispatch(this.actions.removeDocumentSuccess(id))
        return null;
      });
  }
}
