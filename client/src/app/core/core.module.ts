import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from './services/auth.service';
import { HttpService } from './services/http.service';
import { DocumentService } from './services/document.service';
import { XHRBackend, RequestOptions } from '@angular/http';
import { JwtHelperService, JwtModule } from '@auth0/angular-jwt';
import { environment } from '../../environments/environment';
import { NotificationService } from '../shared/components/notification/notification.service';
import { SharedModule } from '../shared/shared.module';
import { UserService } from './services/user.service';

export function httpInterceptor(
  backend: XHRBackend,
  defaultOptions: RequestOptions,
) {
  return new HttpService(backend, defaultOptions);
}

@NgModule({
  imports: [
    CommonModule,
    SharedModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          return localStorage.getItem('token');
        },
        whitelistedDomains: [environment.API_ENDPOINT]
      }
    })
  ],
  providers: [
    AuthService,
    HttpService,
    DocumentService,
    UserService,
    JwtHelperService,
    {
      provide: HttpService,
      useFactory: httpInterceptor,
      deps: [ XHRBackend, RequestOptions]
    },
  ],
  declarations: [
  ]
})
export class CoreModule { }
