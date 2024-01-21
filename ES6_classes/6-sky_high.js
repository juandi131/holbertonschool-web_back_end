import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  set floors(floors) {
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
