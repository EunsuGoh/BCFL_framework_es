var Crowdsource = artifacts.require("./Crowdsource.sol");
var Consortium = artifacts.require("./Consortium.sol");
var Modelcids = artifacts.require("./Modelcids.sol");
var NFTs = artifacts.require("./NFTs.sol");

module.exports = async function(deployer) {
  let crowdsource = deployer.deploy(Crowdsource);
  let consortium = deployer.deploy(Consortium);
  let modelcids = deployer.deploy(Modelcids);
  let nfts = deployer.deploy(NFTs);
  await Promise.all([crowdsource, consortium, modelcids, nfts]);
};