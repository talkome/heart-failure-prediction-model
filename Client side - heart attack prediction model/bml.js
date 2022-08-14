// https://github.com/bigmlcom/bigml-node/blob/master/docs/index.md
// https://www.dataem.com/bigml
// Don't run the all code all the time - produce a model ONCE and use for predictions from now on
// Look for an asyc version.

var bigml = require('bigml');
const { addResiduals } = require('bigml/lib/mathOps');
const controller = require('./controllers/controller')
let instance = null;

// replace the username and the API KEY of your own
var connection = new bigml.BigML('AHMADMSALHA90', '01b068a9d38cb158ff6aa2f497ebf250d20a04c0')
var myModelInfo;

class bigmlm {

  static getbigmlServiceInstance() {
    return instance ? instance : new bigmlm();
  }

initMl () {
  //controller.datatocsv();
  var source = new bigml.Source(connection);
  source.create('./heart.csv', function (error, sourceInfo) {
    if (!error && sourceInfo) {
      var dataset = new bigml.Dataset(connection);
      dataset.create(sourceInfo, function (error, datasetInfo) {
        if (!error && datasetInfo) {
          var model = new bigml.Model(connection);
          model.create(datasetInfo, function (error, modelInfo) {
            if (!error && modelInfo) {
              myModelInfo = modelInfo;
              console.log(myModelInfo);
            }
          });
        }
      });
    }
  });
}

async myPrediction(data)  {
  const Predict = await new Promise((resolve, reject) => {
    if (myModelInfo) {
      var prediction = new bigml.Prediction(connection);
      prediction.create(myModelInfo, {"Age":Number(data.age),"Sex":data.gander,"ChestPainType":data.ChestPainType,"RestingBP":data.RestingBP,"Cholesterol":data.Cholesterol,"FastingBS":data.FastingBS,"RestingECG":data.RestingECG,"MaxHR":data.MaxHR,"ExerciseAngina":data.ExerciseAngina,"Oldpeak":data.Oldpeak,"ST_Slope":data.ST_Slope}, function (error, pred) { 
        
        resolve(pred.object.output) });
    }
    
    
  })
  return Predict
}
}
module.exports = bigmlm;
