import { Component, OnInit } from '@angular/core';
import { UserService } from '../../core/services/user.service';
import { User } from '../../shared/models/users.model';
import { Observable } from 'rxjs/Observable';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {
  users$: Observable<User[]>;
  constructor(
    private userService: UserService,
    private modalService: NgbModal
  ) {
    this.users$ = this.userService.getUserList();
  }

  ngOnInit() {
  }
  openModal(content, user: User) {
    this.modalService.open(content).result.then((result: string) => {
      if (result == 'Confirm') {
        console.log ('Should be deleted', user);
      }
    });
  }
}
