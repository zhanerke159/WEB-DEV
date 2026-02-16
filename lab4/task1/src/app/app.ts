import { Component } from '@angular/core';
import { ReversePipe } from './reverse.pipe';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `Reverse Machine: {{ word | reverse }}`,
  imports: [ReversePipe],
})
export class App {
  word = 'You are a champion';
}
