import {Component, ElementRef, HostListener, OnDestroy, OnInit, ViewChild} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from '../../../shared/models/users.model';
import { Subscription } from 'rxjs/Subscription';
import { UserService } from '../../../core/services/user.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../../core/services/auth.service';

@Component({
  selector: 'app-user-edit',
  templateUrl: './user-edit.component.html',
  styleUrls: ['./user-edit.component.scss']
})
export class UserEditComponent implements OnInit, OnDestroy {

  subscription: Subscription;
  userChangeSubscription: Subscription;
  user: User;
  userChanged: User;
  @ViewChild('editEmail')
  email: ElementRef;
  @ViewChild('editUsername')
  username: ElementRef;
  @ViewChild('editRole')
  role: ElementRef;
  @ViewChild('editPhone')
  phone: ElementRef;
  @ViewChild('editAddress')
  address: ElementRef;
  @ViewChild('editFirstName')
  firstname: ElementRef;
  @ViewChild('editLastName')
  lastname: ElementRef;

  userEditInfoForm: FormGroup;
  userChangePasswordForm: FormGroup;

  private innerHeight: number;
  private userId: number;
  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private authService: AuthService,
    private router : ActivatedRoute
  ) {
    this.subscription = this.router.params.subscribe((params: any) => {
      this.userId = params['id'] || authService.getUserData().id;
      this.userService
        .getUserData(this.userId)
        .subscribe(res => this.user = res as User);
    });
    this.innerHeight = window.innerHeight;
  }
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerHeight = window.innerHeight;
  }
  ngOnInit() {
    this.initUserEditForm();
    this.initChangePasswordForm();
  }
  initUserEditForm() {
    const email = '',
          first_name = '', last_name = '',
          username = '', phone = '',
          address = '', role = 0;

    this.userEditInfoForm = this.fb.group({
        'email': [email, Validators.compose([Validators.required, Validators.email]) ],
        'phone': [phone, Validators.compose([Validators.required, Validators.minLength(11), Validators.maxLength(11), Validators.pattern('[0-9]{11}')]) ],
        'first_name': [first_name],
        'last_name': [last_name],
        'username': [username, Validators.required],
        'address': [address],
        'role': [role, Validators.required],
      }
    );
  }
  initChangePasswordForm() {
    const password = '';
    const password1 = '';
    const password2 = '';

    this.userChangePasswordForm = this.fb.group({
        'password': [password, Validators.compose([Validators.required, Validators.minLength(8)]) ],
        'password1': [password1, Validators.compose([Validators.required, Validators.minLength(8)]) ],
        'password2': [password2, Validators.compose([Validators.required, Validators.minLength(8)]) ],
      },{validator: this.matchingPasswords('password1', 'password2')}
    );
  }
  onSubmit() {
    const values = this.userEditInfoForm.value;
    const keys = Object.keys(values);
    if (this.userEditInfoForm.valid) {
      console.log (this.userEditInfoForm);
      /*this.userChangeSubscription = this.authService.register(values).subscribe(data => {
        const errors = data;
        console.log (data);
        if (errors) {
          keys.forEach(val => {
            if (errors[val]) { this.pushErrorFor(val, errors[val][0]); };
          });
        }
      });*/
    } else {
      keys.forEach(val => {
        const ctrl = this.userEditInfoForm.controls[val];
        if (!ctrl.valid) {
          this.pushErrorFor(val, null);
          ctrl.markAsTouched();
        };
      });
    }
  }

  submitForm() {
    this.userChanged = this.user;
    this.userChanged.email = this.email.nativeElement.value;
    this.userChanged.username = this.username.nativeElement.value;
    this.userChanged.role = this.role.nativeElement.value;
    this.userChanged.phone = this.phone.nativeElement.value;
    this.userChanged.address = this.address.nativeElement.value;
    this.userChanged.first_name = this.firstname.nativeElement.value;
    this.userChanged.last_name = this.lastname.nativeElement.value;
    this.userService.setUserData(JSON.parse(JSON.stringify(this.userChanged))).subscribe();
  }

  private pushErrorFor(ctrl_name: string, msg: string) {
    console.log (ctrl_name, msg)
    if (this.userEditInfoForm.controls[ctrl_name])
      this.userEditInfoForm.controls[ctrl_name].setErrors({'msg': msg});
    else this.userChangePasswordForm.controls[ctrl_name].setErrors({'msg': msg});
  }
  onPasswordChange() {
    const values = this.userChangePasswordForm.value;
    const keys = Object.keys(values);
    if (this.userChangePasswordForm.valid) {
      console.log (this.userChangePasswordForm);
      /*this.userChangeSubscription = this.authService.register(values).subscribe(data => {
       const errors = data;
       console.log (data);
       if (errors) {
       keys.forEach(val => {
       if (errors[val]) { this.pushErrorFor(val, errors[val][0]); };
       });
       }
       });*/
    } else {
      keys.forEach(val => {
        const ctrl = this.userChangePasswordForm.controls[val];
        if (!ctrl.valid) {
          this.pushErrorFor(val, null);
          ctrl.markAsTouched();
        };
      });
    }
  }

  matchingPasswords(passwordKey: string, confirmPasswordKey: string) {
    return (group: FormGroup): {[key: string]: any} => {
      let password = group.controls[passwordKey];
      let confirmPassword = group.controls[confirmPasswordKey];

      if (password.value !== confirmPassword.value) {
        return {
          mismatchedPasswords: true
        };
      }
    }
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
    if (this.userChangeSubscription) {
      this.userChangeSubscription.unsubscribe();
    }
  }
}
