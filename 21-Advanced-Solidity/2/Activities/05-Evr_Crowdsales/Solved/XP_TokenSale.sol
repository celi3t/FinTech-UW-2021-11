pragma solidity ^0.5.0;

import "./XP_TokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract XP_TokenSale is Crowdsale, MintedCrowdsale {

    constructor(
        uint rate, // rate in TKNbits
        address payable wallet, // sale beneficiary
        XP_Token token // the XP_Token itself that the XP_TokenSale will work with
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }
}

contract XP_TokenSaleDeployer {

    address public xp_sale_address;
    address public token_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    )
        public
    {
        // create the XP_Token and keep its address handy
        XP_Token token = new XP_Token(name, symbol, 0);
        token_address = address(token);

        // create the XP_TokenSale and tell it about the token
        XP_TokenSale xp_sale = new XP_TokenSale(1, wallet, token);
        xp_sale_address = address(xp_sale);

        // make the XP_TokenSale contract a minter, then have theXP_TokenSaleDeployer renounce its minter role
        token.addMinter(xp_sale_address);
        token.renounceMinter();
    }
}
