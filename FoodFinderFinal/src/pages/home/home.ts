import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {foodPage} from '../food/food';
import { restaurantsPage } from '../restaurants/restaurants';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController) {

  }

  openrestaurantpage(){
    this.navCtrl.push(restaurantsPage)
  }

  openfoodpage(){
    this.navCtrl.push(foodPage)
  }

}
