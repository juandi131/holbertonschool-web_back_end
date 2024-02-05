
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}

class getNeighborhoodsList {
  constructor() {
    this.neighborhoods = [];
  }

  addNeighborhood(neighborhood) {
    this.neighborhoods.push(neighborhood);
    return this.neighborhoods;
  }
}

const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res);
