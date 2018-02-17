export class Notification {
  title: string = null;
  type: string = 'notification--message';
  message: string = null;
  delay: number = 5000;
  state = 'hidden';

  constructor(title: string, type? : string, message?: string, delay?: number) {
    this.title = title;
    this.type = 'notification--'+type;
    if (!message || message === "") {
      this.type += ' notification--title-only';
    }

    this.message = message;
    this.delay = delay;
  }
  toggleState() {
    this.state = this.state === 'shown' ? 'hidden' : 'shown';
  }
}
