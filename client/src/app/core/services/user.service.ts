import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { Observable } from 'rxjs/Observable';
import { User } from '../../shared/models/users.model';

@Injectable()
export class UserService {

  constructor(
    private http: HttpService
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

}
