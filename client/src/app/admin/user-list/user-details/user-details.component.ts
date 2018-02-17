import { Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { User } from '../../../shared/models/users.model';
import { ActivatedRoute } from '@angular/router';
import { UserService } from '../../../core/services/user.service';
import { Subscription } from 'rxjs/Subscription';

@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.scss']
})
export class UserDetailsComponent implements OnInit, OnDestroy {
  subscription: Subscription;
  user: User;
  private innerHeight: number;
  private userId: number;
  constructor(

    private userService: UserService,
    private router : ActivatedRoute
  ) {
    this.subscription = this.router.params.subscribe((params: any) => {
      this.userId = params['id'];
      this.userService
        .getUserData(this.userId)
        .subscribe(res => this.user = res as User);
    });
    this.innerHeight =window.innerHeight;
  }
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerHeight = window.innerHeight;
  }
  ngOnInit() {

  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
