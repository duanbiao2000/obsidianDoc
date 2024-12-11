---
promptId: dall-e-core
aliases: 🗞️ dall-e-core
summary: dalle core options
author: 
tags: 
version: 0.0.1
disableProvider: true
viewTypes:
  - none
---

```json:form
{
	"title": "Widgets",
	required:[
		"tg_selection",
		"model"
	],

	"properties": {
		tg_selection:{
			title: "tg_selection",
			type: "string",
		},
		model: {
	      "title": "Model",
	      "type": "string",
	      oneOf: [
	        {
	          "const": "dall-e-3",
	          "title": "Dall-e 3"
	        },
	        {
	          "const": "dall-e-2",
	          "title": "Dall-e 2"
	        },
	      ]
	    }
	},
  
	uiSchema: {
		tg_selection:{
			"ui:widget": "textarea",
            props: {
              className: "w-full"
            }
		},
		model: {
			"ui:enumDisabled": [
				"multiply"
			]
		},
	},
	
	formData: {
		model: "dall-e-3"
	},
}
```

Variables used:
{{tg_selection}}


***

***

{{#script}}

```js
const OPENAI_API_KEY = plugin.getApiKeys().openAIChat;
if(!OPENAI_API_KEY?.length) throw "no apikey provided in the OpenAIChat LLM Provider"


const prompt = this.tg_selection;

try {
    // Set up the request headers and body
    const requestOptions = {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${OPENAI_API_KEY}`,
        'Content-Type': 'application/json',
      },

      body: JSON.stringify({
        model: 'dall-e-3',
        prompt,
        n: 1,
        size: '1024x1024'
      })
    };

    // Make the request to OpenAI's API
    const response = await fetch('https://api.openai.com/v1/images/generations', requestOptions);

    if (!response.ok) {
      throw new Error(`OpenAI API request failed with status ${response.status}`);
    }

    // Get the image data from the response
    const imageData = await response.json();

    // Assuming the API returns a URL or binary data for the image
    const imageBinary = await requestUrl(imageData.data[0].url).then(res=>res.arrayBuffer)

    // Generate a random file name
    const randomFileName = `generated-image-${Math.random().toString(36).substring(2, 15)}.png`;

    const filePath = `images/${randomFileName}`; // Prepend the "images" directory to the file name

    // Use the Vault API to save the image file
    const vault = app.vault; // Assuming this script has access to `app` from the environment

    // Check if the "images" directory exists, if not, create it
    let imagesDir = vault.getAbstractFileByPath('images');

    if (!imagesDir) {
      await vault.createFolder('images');
    }

    // Check if file exists, if so, remove it before writing new content

    let existingFile = vault.getAbstractFileByPath(filePath);

    if (existingFile && existingFile instanceof TFile) {
      await vault.delete(existingFile);
    }
    
    await vault.createBinary(filePath, new Uint8Array(imageBinary));
    return filePath;
    
} catch (error) {
    console.error('Error generating or saving image:', error);
}

// Call the function to generate an image and save it in the vault
return await generateDalleImageAndSaveToVault(IMAGE_PROMPT);
```

{{/script}}