import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';
import { Notification } from './notification.model';

@Injectable()
export class NotificationService {
  notifications$: Subject<Notification>;
  constructor() {
    this.notifications$ = new Subject();
  }

  sendMessage(title, type, message, time) {
    this.notifications$.next(new Notification(title, type, message, time));
  }

}
