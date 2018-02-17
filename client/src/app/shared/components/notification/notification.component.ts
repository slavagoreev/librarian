import { Component, Input, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { HttpService } from "../../../core/services/http.service";
import { Notification } from './notification.model';
import { Observable } from 'rxjs/Observable';
import * as _ from "lodash";
import {
  trigger,
  state,
  style,
  animate,
  transition, stagger, keyframes
} from '@angular/animations';
import { NotificationService } from './notification.service';

@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.scss'],
  animations: [
    trigger('notificationState', [
      transition('void => *', [
        animate('.4s ease-in', keyframes([
          style({opacity: 0, transform: 'translateX(75%)', offset: 0}),
          style({opacity: .5, transform: 'translateX(-35px)',  offset: 0.3}),
          style({opacity: 1, transform: 'translateX(0)',     offset: 1.0}),
        ]))
      ]),
      transition('* => void', [
        animate('.4s ease-out', keyframes([
          style({opacity: 1, transform: 'translateX(0)', offset: 0}),
          style({opacity: .5, transform: 'translateX(-35px)',  offset: 0.3}),
          style({opacity: 0, transform: 'translateX(75%)',     offset: 1.0}),
        ]))
      ])
    ])
  ]
})

export class NotificationComponent implements OnInit {
  @Input() data: Notification;
  notifications: Notification[] = [];

  constructor(
    private httpInterceptor: HttpService,
    private notificationsService: NotificationService
  ) {
    this.httpInterceptor.loading.subscribe(data => {
      if (data.error) {
        const delay = data.error.delay || 5000;
        const notification = new Notification(
          data.error.title,
          "error",
          data.error.message,
          delay);
        this.notifications.unshift(notification);
        setTimeout(() => {
          this.notifications = _.without(this.notifications, notification)
        }, delay)
      }
    });

    this.notificationsService.notifications$.subscribe((notification) => {
      this.notifications.unshift(notification);
      setTimeout(() => {
        this.notifications = _.without(this.notifications, notification)
      }, notification.delay)
    });
  }
  removeItem(i) {
    this.notifications.splice(i, 1);
  }

  ngOnInit() {
  }

  ngOnDestroy() {
  }


}
