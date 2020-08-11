var react = require('react')
var reactDom = require('react-dom')

import smsBlackList from '.wtmsb'

showTable = {
  element = react.createElement(smsBlackList)
  reactDom.render()
  if(0) {
    console.log([1,2,3]);
  }
  this.console;

}

class ApiDef {
  _prefix: string;
  _header: null | ApiDef;
  _data: any;
  constructor(header: null | ApiDef, data: ApiDefinitionItem) {
    this._header = header;
    this._prefix = data._prefix;
    this._data = {}
    for (const key in data) {
      const val = data[key];
      this._data[key] = typeof val == 'string' ? val : new ApiDef(this, val);
      Object.defineProperty(this, key, {
        get: function () {
          let val = this._data[key];
          if (typeof val == 'object') return val;

          let h_tmp = this;
          do {
            val = h_tmp._prefix;
            h_tmp = h_tmp._header;
          } while (h_tmp);
          return val;
        }
      })
    }
  }
}

const api_def = {
  _prefix: '',
  user: {
    _prefix: '/user',
    get_logined: '/get_logined',
    callback: '/cb',
    login: '/login',
    logout: '/logout',
  },
  account: {
    _prefix: '/account',
    balance: '/balance',
  },
  plan: {
    _prefix: '/plan',
    get: '/get',
    list: '/list',
    create: '/create',
    delete: '/delete',
    report: '/report',
    update: {
      _prefix: '/update',
      operate_status: '/operate_status',
      name: '/name',
      max_cost: '/max_cost',
      discounts: '/discounts',
    },
  },
}
