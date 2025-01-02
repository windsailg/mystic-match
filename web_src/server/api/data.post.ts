import { sendError } from 'h3'
import axios from 'axios'
import { readConfig } from 'browserslist'
export default defineEventHandler(async event => {
  const config = useRuntimeConfig()
  // Image 資料可以存到 public 資料夾，並直接使用路徑即可　不需要額外資料庫
  // EX: public/images/main-banner.jpg
  const data = {
    comments: '這套穿搭展現了恬靜與自然的氛圍，整體色調柔和，給人一種輕鬆愜意的感覺。同時，配件的選擇也十分用心，為整體增添了一點亮點。這樣的風格不僅適合日常，也能讓人感覺到穿者的自信與從容。',
    mainRecommand:
      'https://i5.walmartimages.com/asr/b92f9576-e46b-481a-a4b9-c36eacdccdcb.f14966b8f06667383f0dc818c4c263c1.jpeg?odnHeight=2000&odnWidth=2000&odnBg=FFFFFF',
    recommandList: [
      'https://mamarentals.com.au/cdn/shop/files/Mama-Rentals-Tea-Princess-Eve-Two-Piece-Set-2..jpg?crop=center&height=975&v=1695196580&width=650',
      'https://mamarentals.com.au/cdn/shop/files/Mama-Rentals-Tea-Princess-Eve-Two-Piece-Set-1..jpg?crop=center&height=975&v=1695196581&width=650',
      'https://mamarentals.com.au/cdn/shop/files/Mama-Rentals-Tea-Princess-Eve-Two-Piece-Set-6..jpg?crop=center&height=975&v=1695196576&width=650',
      'https://mamarentals.com.au/cdn/shop/files/Mama-Rentals-Tea-Princess-Eve-Two-Piece-Set-3..jpg?crop=center&height=975&v=1695196571&width=650'
    ]
  }
  return {
    statusCode: 200,
    statusMessage: 'OK',
    result: data
  }
})
// test...