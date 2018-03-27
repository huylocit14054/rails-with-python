Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  root :to => 'factorial#new'
  post 'factorial_loc' , to: 'factorial#calculate_factorial' 
  get 'factorial_loc' , to: 'factorial#new' 
end
