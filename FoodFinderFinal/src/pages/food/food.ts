import { Component, NgZone } from '@angular/core';
import { NavController, Events } from 'ionic-angular';
import {Http} from "@angular/http"
import 'rxjs/add/operator/map'


@Component({
  selector: 'page-food',
  templateUrl: 'food.html'
})
export class foodPage {
  
  food:any;
  result= [];
  constructor(public navCtrl: NavController, public http: Http, private _ngZone: NgZone, public events: Events) {

    if(this.food == undefined){
        this.events.subscribe('updateScreen', () => {
        this._ngZone.run(() => {
          //this.navCTLR.push(HomePage);
          console.log('force update the screen');
        });
      });
      this.getFoods();
      }
  }

 
  getFoods(){

    this.http.get('http://127.0.0.1:8000/foods/').map(res=> res.json()).subscribe(data => { this.food=data;
    for(var i=0; i < this.food.length; i++){
      
      this.result.push('Food: ' + this.food[i].name);
    }
    console.log(this.result);
    this.events.publish('updateScreen');
    return this.result;
   });
  }

  
 }
