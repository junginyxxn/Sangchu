//
//  HomeNetworkManager.swift
//  상추 - 상권추천서비스
//
//  Created by 양희태 on 3/25/24.
//
import Foundation
import Alamofire

class HomeNetworkManager {
    static let shared = HomeNetworkManager()
    private let BASE_URL = "http://3.36.91.181:8084/api"
    
    func fetch(endpoint: String?, completion: @escaping (Result<Data, Error>) -> Void) {
        if let endpoint {
            let urlString = "\(BASE_URL)\(endpoint)"
            print(urlString)
            AF
                .request(urlString)
                .validate()
                .responseData { response in
                switch response.result {
                    case .success(let data):
                    print("성공")
                        completion(.success(data))
                    case .failure(let error):
                    print("실패")
                        completion(.failure(error))
                }
            }
        }
        else {
            print("잘못된 엔드포인트 매개변수입니다.")
        }
    }
    
}
