# coding: utf-8

# flake8: noqa

"""
    GMO Aozora Net Bank Open API

    <p>オープンAPI仕様書（PDF版）は下記リンクをご参照ください</p> <div>   <div style='display:inline-block;'><a style='text-decoration:none; font-weight:bold; color:#00b8d4;' href='https://gmo-aozora.com/business/service/api-specification.html' target='_blank'>オープンAPI仕様書</a></div><div style='display:inline-block; margin-left:2px; left:2px; width:10px; height:10px; border-top:2px solid #00b8d4; border-right:2px solid #00b8d4; transparent;-webkit-transform:rotate(45deg); transform: rotate(45deg);'></div> </div> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>共通仕様</h4> <div style='width:100%; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>＜HTTPリクエストヘッダ＞</p>   <div style='display:table; margin-left:10px; background-color:#29659b;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff;'>項目</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; color:#fff;'>仕様</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>プロトコル</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>HTTP1.1/HTTPS</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>charset</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>UTF-8</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>content-type</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>application/json</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>domain_name</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       本番環境：api.gmo-aozora.com</br>       開発環境：stg-api.gmo-aozora.com     </div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>メインURL</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       https://{domain_name}/ganb/api/corporation/{version}</br>       <span style='border-bottom:solid 1px;'>Version:1.x.x</span> の場合</br>       　https://api.gmo-aozora.com/ganb/api/corporation/<span style='border-bottom:solid 1px;'>v1</span>     </div>   </div> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜リクエスト共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <p style='padding-left:40px;'>パラメータの値が空の場合、またはパラメータ自体が設定されていない場合、どちらもNULLとして扱います</p> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜レスポンス共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <ul>     <li>レスポンスデータ</li>       <ul>         <li style='list-style-type:none;'>レスポンスデータの値が空の場合または、レスポンスデータ自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>     <li>配列</li>       <ul>         <li style='list-style-type:none;'>配列の要素の値が空の場合は「空のリスト」と記載</li>         <li style='list-style-type:none;'>配列自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>   </ul> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜更新系APIに関する注意事項＞</p>   <ul>     <li style='list-style-type:none;'>更新系処理がタイムアウトとなった場合、処理自体は実行されている可能性がありますので、</li>     <li style='list-style-type:none;'>再実行を行う必要がある場合は必ず照会系の処理で実行状況を確認してから再実行を行ってください</li>   </ul> </div>   # noqa: E501

    OpenAPI spec version: 1.1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from ganb_corporate_client.api.account_api import AccountApi
from ganb_corporate_client.api.bulk_transfer_api import BulkTransferApi
from ganb_corporate_client.api.transfer_api import TransferApi
from ganb_corporate_client.api.virtual_account_api import VirtualAccountApi

# import ApiClient
from ganb_corporate_client.api_client import ApiClient
from ganb_corporate_client.configuration import Configuration
# import models into sdk package
from ganb_corporate_client.models.account import Account
from ganb_corporate_client.models.accounts_response import AccountsResponse
from ganb_corporate_client.models.balance import Balance
from ganb_corporate_client.models.balances_response import BalancesResponse
from ganb_corporate_client.models.bulk_transfer import BulkTransfer
from ganb_corporate_client.models.bulk_transfer_detail import BulkTransferDetail
from ganb_corporate_client.models.bulk_transfer_info import BulkTransferInfo
from ganb_corporate_client.models.bulk_transfer_request import BulkTransferRequest
from ganb_corporate_client.models.bulk_transfer_request_response import BulkTransferRequestResponse
from ganb_corporate_client.models.bulk_transfer_response import BulkTransferResponse
from ganb_corporate_client.models.bulk_transfer_status_response import BulkTransferStatusResponse
from ganb_corporate_client.models.deposit_transactions_response import DepositTransactionsResponse
from ganb_corporate_client.models.error_detail import ErrorDetail
from ganb_corporate_client.models.error_response import ErrorResponse
from ganb_corporate_client.models.payment_arrival import PaymentArrival
from ganb_corporate_client.models.request_transfer_status import RequestTransferStatus
from ganb_corporate_client.models.transaction import Transaction
from ganb_corporate_client.models.transactions_response import TransactionsResponse
from ganb_corporate_client.models.transfer import Transfer
from ganb_corporate_client.models.transfer_accept import TransferAccept
from ganb_corporate_client.models.transfer_apply import TransferApply
from ganb_corporate_client.models.transfer_apply_detail import TransferApplyDetail
from ganb_corporate_client.models.transfer_cancel_request import TransferCancelRequest
from ganb_corporate_client.models.transfer_cancel_response import TransferCancelResponse
from ganb_corporate_client.models.transfer_detail import TransferDetail
from ganb_corporate_client.models.transfer_detail_response import TransferDetailResponse
from ganb_corporate_client.models.transfer_error import TransferError
from ganb_corporate_client.models.transfer_error_detail import TransferErrorDetail
from ganb_corporate_client.models.transfer_fee_detail import TransferFeeDetail
from ganb_corporate_client.models.transfer_fee_response import TransferFeeResponse
from ganb_corporate_client.models.transfer_info import TransferInfo
from ganb_corporate_client.models.transfer_query_bulk_response import TransferQueryBulkResponse
from ganb_corporate_client.models.transfer_request import TransferRequest
from ganb_corporate_client.models.transfer_request_response import TransferRequestResponse
from ganb_corporate_client.models.transfer_request_result_response import TransferRequestResultResponse
from ganb_corporate_client.models.transfer_response import TransferResponse
from ganb_corporate_client.models.transfer_status_response import TransferStatusResponse
from ganb_corporate_client.models.unable_detail_info import UnableDetailInfo
from ganb_corporate_client.models.v_account import VAccount
from ganb_corporate_client.models.va import Va
from ganb_corporate_client.models.va_close_request import VaCloseRequest
from ganb_corporate_client.models.va_close_request_response import VaCloseRequestResponse
from ganb_corporate_client.models.va_deposit_transactions_response import VaDepositTransactionsResponse
from ganb_corporate_client.models.va_id import VaId
from ganb_corporate_client.models.va_issue_request import VaIssueRequest
from ganb_corporate_client.models.va_issue_response import VaIssueResponse
from ganb_corporate_client.models.va_list_request import VaListRequest
from ganb_corporate_client.models.va_list_response import VaListResponse
from ganb_corporate_client.models.va_status_change_request import VaStatusChangeRequest
from ganb_corporate_client.models.va_status_change_response import VaStatusChangeResponse
from ganb_corporate_client.models.va_status_code import VaStatusCode
from ganb_corporate_client.models.va_transaction import VaTransaction
from ganb_corporate_client.models.visa_transaction import VisaTransaction
from ganb_corporate_client.models.visa_transactions_response import VisaTransactionsResponse
