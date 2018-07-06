import { Component, NgZone } from '@angular/core';
import { NavController, Events } from 'ionic-angular';
import {Http} from "@angular/http"
import 'rxjs/add/operator/map'

@Component({
  selector: 'page-restaurants',
  templateUrl: 'restaurants.html'
})
export class restaurantsPage {
  food:any;
  restaurants: any;
  result= [];
  constructor(public navCtrl: NavController, public http: Http, private _ngZone: NgZone, public events: Events) {

    if(this.restaurants == undefined){
        this.events.subscribe('updateScreen', () => {
        this._ngZone.run(() => {
          //this.navCTLR.push(HomePage);
          console.log('force update the screen');
        });
      });
      this.getRestaurants();
      }
  }

  getRestaurants(){
       
    this.http.get('http://127.0.0.1:8000/restaurants/').map(res=> res.json()).subscribe(data => {
      this.restaurants = data;
      for(var i=0; i < this.restaurants.length; i++){
      
        this.result.push(['Restaurant: ' + this.restaurants[i].name  +' Location: ' + this.restaurants[i].location]);
      }
      console.log(this.result);
      this.events.publish('updateScreen');
      return this.result;
  });
  }

 
  




}