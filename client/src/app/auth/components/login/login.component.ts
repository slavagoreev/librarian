import { Component, OnInit, OnDestroy, HostListener } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../../../core/services/auth.service';
import { Store } from '@ngrx/store';
import { AppState } from '../../../interfaces';
import { Router, ActivatedRoute } from '@angular/router';
import { getAuthStatus } from '../../reducers/selectors';
import { Subscription } from 'rxjs/Subscription';
import {HttpService} from "../../../core/services/http.service";
import {Http, Response} from "@angular/http";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy {
  innerHeight: number;
  signInForm: FormGroup;
  title = environment.AppName;
  loginSubs: Subscription;

  constructor(
    private fb: FormBuilder,
    private store: Store<AppState>,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthService,
    private http: HttpService
  ) {
    this.redirectIfUserLoggedIn();
    this.innerHeight = window.innerHeight;
  }
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerHeight = window.innerHeight;
  }

  ngOnInit() {
    this.initForm();
    // get return url from route parameters or default to '/'
  }

  onSubmit() {
    const values = this.signInForm.value;
    const keys = Object.keys(values);

    if (this.signInForm.valid) {
      // console.error(newWindow);
      // console.log(newWindow);
      this.loginSubs = this.authService.login(values).subscribe(data => {
        const error = data.error;
        if (error) {
          keys.forEach(val => {
            this.pushErrorFor(val, error);
          });
        }
      });
    } else {
      keys.forEach(val => {
        const ctrl = this.signInForm.controls[val];
        if (!ctrl.valid) {
          this.pushErrorFor(val, null);
          ctrl.markAsTouched();
        };
      });
    }
  }


  private pushErrorFor(ctrl_name: string, msg: string) {
    this.signInForm.controls[ctrl_name].setErrors({'msg': msg});
  }

  initForm() {
    const username = '';
    const password = '';

    this.signInForm = this.fb.group({
      'username': [username, Validators.required],
      'password': [password, Validators.required]
    });
  }

  redirectIfUserLoggedIn() {
    this.store.select(getAuthStatus).subscribe(
      data => {
        if (data === true) { this.router.navigate(['/documents']);}
      }
    );
  }

  ngOnDestroy() {
    if (this.loginSubs) { this.loginSubs.unsubscribe(); }
  }

}
